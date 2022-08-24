const axios=require('axios');
const chalk=require('chalk');
const figlet=require('figlet');

figlet('PingJS',function(err,data) {
    if (err) {
        console.log('Something went wrong...');
        console.dir(err);
        return;
    }
    console.log(chalk.yellow(data));
});

const target=process.argv[2];

function ping(url){    
  if(!url.includes('http')){
    url='https://'+url;
  }    
    axios.get(url,{timeout:10000})
      .then((response)=>{
        console.log(`${chalk.blueBright(url)} is ${chalk.greenBright('up')}.`);
        ping(url);
      })
      .catch((error)=>{
        console.log(`${chalk.blueBright(url)} is ${chalk.redBright('down')}.`);
        ping(url);
      });
}

ping(target);