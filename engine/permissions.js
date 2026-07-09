const fs=require('fs'); const path=require('path'); const crypto=require('crypto'); const {loadConfig,ensureDir,writeReceipt}=require('./paths');
function id(){return crypto.randomBytes(8).toString('hex');}
function stagePermission(kind,action,payload={}){const cfg=loadConfig(); const dir=ensureDir(path.join(cfg.workspaceRoot,'permissions','pending')); const packet={id:id(),kind,action,payload,status:'pending',createdAt:new Date().toISOString(),law:'operator_approval_required'}; const file=path.join(dir,`${packet.id}_${kind}.json`); fs.writeFileSync(file,JSON.stringify(packet,null,2)); const receipt=writeReceipt(cfg,'permission_stage',{packet,file}); return {packet,file,receipt};}
module.exports={stagePermission};
