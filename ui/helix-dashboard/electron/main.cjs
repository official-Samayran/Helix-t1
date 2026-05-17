const { app, BrowserWindow, Tray, Menu } = require('electron')
const path = require('path')

let mainWindow
let tray

const gotTheLock = app.requestSingleInstanceLock()

if (!gotTheLock) {
  app.quit()
  process.exit(0)
}

function createWindow() {

  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    show: true,
    autoHideMenuBar: true,
    backgroundColor: '#0a0a0a',
    webPreferences: {
      contextIsolation: true,
      nodeIntegration: false
    }
  })

  mainWindow.loadURL('http://localhost:5173')

  mainWindow.webContents.on(
    'render-process-gone',
    () => {
      console.log('Renderer crashed')
    }
  )

  mainWindow.webContents.on(
    'did-fail-load',
    () => {
      console.log('Failed loading UI')
    }
  )

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

  const iconPath = path.join(
    __dirname,
    'icon.png'
  )

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
    }

    else {
      mainWindow.show()
    }

  })
}

app.whenReady().then(() => {

  createWindow()

  createTray()

})

app.on('window-all-closed', (e) => {
  e.preventDefault()
})