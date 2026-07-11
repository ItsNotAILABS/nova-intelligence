const child_process=require('child_process'); const path=require('path'); const {loadConfig,writeReceipt}=require('./paths');
const ALLOWED=[/^npm\s+(test|run\s+test|run\s+build|run\s+validate)$/,/^node\s+scripts\/validate\.js$/,/^node\s+engine\/cli\.js\s+repo-index\s+\.$/];
function sandboxExecute(command,cwd){const cfg=loadConfig(); const ok=ALLOWED.some(r=>r.test(command.trim())); if(!ok){return {allowed:false,staged:true,reason:'command_not_allowlisted',receipt:writeReceipt(cfg,'sandbox_denied',{command,cwd})};}
 const root=path.resolve(cwd||process.cwd()); const res=child_process.spawnSync(command,{cwd:root,shell:true,timeout:20000,encoding:'utf8'}); const out={allowed:true,code:res.status,stdout:(res.stdout||'').slice(-4000),stderr:(res.stderr||'').slice(-4000)}; out.receipt=writeReceipt(cfg,'sandbox_execute',{command,cwd:root,result:out}); return out;}
module.exports={sandboxExecute};
