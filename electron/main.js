const {app,BrowserWindow}=require('electron'); const child_process=require('child_process'); const path=require('path'); let server;
function create(){server=child_process.spawn(process.execPath,[path.join(__dirname,'..','engine','local_server.js')],{stdio:'inherit'}); const win=new BrowserWindow({width:1200,height:800,webPreferences:{preload:path.join(__dirname,'preload.js')}}); setTimeout(()=>win.loadURL('http://127.0.0.1:8765'),1000)}
app.whenReady().then(create); app.on('window-all-closed',()=>{if(server)server.kill(); app.quit();});
