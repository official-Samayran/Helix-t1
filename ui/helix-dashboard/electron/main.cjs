const { app, BrowserWindow, Tray, Menu } = require("electron")
const path = require("path")

let mainWindow
let tray

function createWindow() {

    mainWindow = new BrowserWindow({
        width: 1400,
        height: 900,
        frame: false,
        backgroundColor: "#0a0a0a",
        webPreferences: {
            preload: path.join(__dirname, "preload.cjs")
        }
    })

    mainWindow.loadURL("http://localhost:5173")

    mainWindow.on("close", (event) => {
        if (!app.isQuiting) {
            event.preventDefault()
            mainWindow.hide()
        }
        return false
    })
}

app.whenReady().then(() => {

    createWindow()

    tray = new Tray(
        path.join(__dirname, "icon.png")
    )

    const contextMenu = Menu.buildFromTemplate([
        {
            label: "Open HELIX",
            click: () => {
                mainWindow.show()
            }
        },
        {
            label: "Quit",
            click: () => {
                app.isQuiting = true
                app.quit()
            }
        }
    ])

    tray.setToolTip("HELIX")

    tray.setContextMenu(contextMenu)

    tray.on("double-click", () => {
        mainWindow.show()
    })
})