const { app, BrowserWindow, Tray, Menu } = require('electron')
const path = require('path')
const { spawn } = require('child_process')
const http = require('http')

let mainWindow
let tray

const gotTheLock = app.requestSingleInstanceLock()

if (!gotTheLock) {
  app.quit()
  process.exit(0)
}

function checkOllamaReady() {
  return new Promise((resolve) => {
    const req = http.get('http://127.0.0.1:11434', () => {
      resolve(true)
    })

    req.on('error', () => {
      resolve(false)
    })

    req.end()
  })
}

async function waitForOllama() {
  let ready = false

  while (!ready) {
    ready = await checkOllamaReady()

    if (!ready) {
      await new Promise((r) => setTimeout(r, 2000))
    }
  }
}

function startOllama() {
  spawn('ollama', ['serve'], {
    detached: true,
    shell: true,
    windowsHide: true
  })
}

function startBackend() {
  spawn('python', ['E:/Helix/main.py'], {
    detached: true,
    shell: true,
    windowsHide: true
  })
}

async function startServices() {
  startOllama()

  await waitForOllama()

  startBackend()
}

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    show: false,
    autoHideMenuBar: true,
    backgroundColor: '#0a0a0a',
    webPreferences: {
      contextIsolation: true,
      nodeIntegration: false
    }
  })

  mainWindow.loadURL('http://localhost:5173')

  mainWindow.on('minimize', (event) => {
    event.preventDefault()
    mainWindow.hide()
  })

  mainWindow.on('close', (event) => {
    event.preventDefault()
    mainWindow.hide()
  })
}

function createTray() {
  const iconPath = path.join(__dirname, 'icon.png')

  tray = new Tray(iconPath)

  const contextMenu = Menu.buildFromTemplate([
    {
      label: 'Open HELIX',
      click: () => {
        mainWindow.show()
      }
    },
    {
      label: 'Hide',
      click: () => {
        mainWindow.hide()
      }
    },
    {
      label: 'Quit',
      click: () => {
        app.exit()
      }
    }
  ])

  tray.setToolTip('HELIX')
  tray.setContextMenu(contextMenu)

  tray.on('click', () => {
    if (mainWindow.isVisible()) {
      mainWindow.hide()
    } else {
      mainWindow.show()
    }
  })
}

app.whenReady().then(async () => {
  await startServices()

  createWindow()

  createTray()
})

app.on('window-all-closed', (e) => {
  e.preventDefault()
})