const {tools}=require('../server/nova_mcp_server');
function toGeminiFunctionDeclarations(){return tools.map(t=>({name:t.name,description:t.description,parameters:t.inputSchema||{type:'object',properties:{}}}));}
function writeGeminiTools(){const fs=require('fs'); const path=require('path'); const out=path.join(__dirname,'..','manifests','gemini_function_declarations.json'); fs.mkdirSync(path.dirname(out),{recursive:true}); fs.writeFileSync(out,JSON.stringify({functionDeclarations:toGeminiFunctionDeclarations()},null,2)); return out;}
if(require.main===module) console.log(writeGeminiTools());
module.exports={toGeminiFunctionDeclarations,writeGeminiTools};
