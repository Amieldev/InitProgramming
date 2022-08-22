const axios=require('axios');
const chalk=require('chalk');

const target=process.argv[2];

function ping(url){    
    axios.get(url)
      .then((response) => {
        console.log(`${chalk.blueBright(url)} is ${chalk.greenBright('up')}.`);
        ping(url);
    })
      .catch((error) => {
        console.log(`${chalk.blueBright(url)} is ${chalk.redBright('down')}.`);
        ping(url);
      });
}

ping(target);