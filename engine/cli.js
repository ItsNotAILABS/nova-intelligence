#!/usr/bin/env node
const fs=require('fs'); const path=require('path'); const {indexRepo,semanticSearch}=require('./repo_intelligence'); const {buildCapsule}=require('./capsule'); const {migrateDownloads}=require('./storage_engine'); const {sandboxExecute}=require('./sandbox'); const {loadConfig,ensureDir}=require('./paths'); const {stagePermission}=require('./permissions');
function saveIndex(root){const cfg=loadConfig(); const idx=indexRepo(root); const out=path.join(ensureDir(path.join(cfg.workspaceRoot,'repo_indexes')),`${path.basename(path.resolve(root))||'repo'}.json`); fs.writeFileSync(out,JSON.stringify(idx,null,2)); console.log(JSON.stringify({ok:true,index:out,fileCount:idx.fileCount},null,2));}
const [,,cmd,...args]=process.argv;
try{
 if(cmd==='status'){const cfg=loadConfig(); console.log(`NOVA Agent Council 0.8 | workspace=${cfg.workspaceRoot} | vault=${cfg.vaultRoot}`)}
 else if(cmd==='repo-index') saveIndex(args[0]||'.');
 else if(cmd==='search'){const idx=JSON.parse(fs.readFileSync(args[0],'utf8')); console.log(JSON.stringify(semanticSearch(idx,args.slice(1).join(' ')),null,2));}
 else if(cmd==='capsule') console.log(JSON.stringify(buildCapsule({name:args[0]||'nova-capsule',title:args[1]||'NOVA Capsule'}),null,2));
 else if(cmd==='storage-dryrun') console.log(JSON.stringify(migrateDownloads({dryRun:true}),null,2));
 else if(cmd==='storage-live') console.log(JSON.stringify(migrateDownloads({dryRun:false}),null,2));
 else if(cmd==='permission') console.log(JSON.stringify(stagePermission(args[0]||'app',args[1]||'requested_action',{args:args.slice(2)}),null,2));
 else if(cmd==='sandbox') console.log(JSON.stringify(sandboxExecute(args.join(' '),process.cwd()),null,2));
 else {console.log('commands: status | repo-index <dir> | search <index.json> <query> | capsule <name> | storage-dryrun | storage-live | permission <kind> <action> | sandbox <cmd>');}
}catch(e){console.error(e.stack||e.message); process.exit(1)}
