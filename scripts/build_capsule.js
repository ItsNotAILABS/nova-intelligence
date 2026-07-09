const {buildCapsule}=require('../engine/capsule'); console.log(JSON.stringify(buildCapsule({name:process.argv[2]||'nova-capsule'}),null,2));
