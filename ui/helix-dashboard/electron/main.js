const { app, BrowserWindow, Tray, Menu, nativeImage } = require('electron')
const path = require('path')
const { spawn } = require('child_process')

let mainWindow
let tray
let backendProcess

const isDev = true

function startBackend() {
  backendProcess = spawn('python', ['E:/Helix/main.py'], {
    detached: true,
    shell: true,
    stdio: 'ignore'
  })

  backendProcess.unref()
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

app.whenReady().then(() => {
  startBackend()
  createWindow()
  createTray()
})

app.on('window-all-closed', (e) => {
  e.preventDefault()
})