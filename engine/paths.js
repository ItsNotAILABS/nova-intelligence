const fs = require('fs');
const path = require('path');
function expandEnv(p){return (p||'').replace(/%([^%]+)%/g,(_,k)=>process.env[k]||`%${k}%`);}
function loadConfig(){const cfg=JSON.parse(fs.readFileSync(path.join(__dirname,'..','config','nova.config.json'),'utf8')); cfg.vaultRoot=expandEnv(cfg.vaultRoot); cfg.workspaceRoot=expandEnv(cfg.workspaceRoot); cfg.managedFolders=(cfg.managedFolders||[]).map(expandEnv); return cfg;}
function ensureDir(p){fs.mkdirSync(p,{recursive:true}); return p;}
function receiptPath(cfg,prefix){const dir=ensureDir(path.join(cfg.vaultRoot,'.nova','receipts')); return path.join(dir,`${prefix}_${new Date().toISOString().replace(/[:.]/g,'-')}.json`);}
function writeReceipt(cfg,prefix,data){const out=receiptPath(cfg,prefix); fs.writeFileSync(out, JSON.stringify({time:new Date().toISOString(),...data},null,2)); return out;}
module.exports={loadConfig,ensureDir,writeReceipt,expandEnv};
