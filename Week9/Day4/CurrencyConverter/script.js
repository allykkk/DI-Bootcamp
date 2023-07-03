const apiKey=''

async function getCurrencies(){
    const url=`https://v6.exchangerate-api.com/v6/${apiKey}/codes`
    const response = await fetch(url);
    const data=await response.json()
    const orginalArray =data.supported_codes
    let object={} 
    orginalArray.forEach(element => {
        object[`${element[0]} - ${element[1]}`] =`${element[0]}`      
    });
    return object // each element looks like : USD-United States Dollar: "USD"
}



async function fillDropDown(id){
    const select=document.getElementById(id)
    const currencyChoices=await getCurrencies();
    Object.keys(currencyChoices).forEach((element)=>{
        const option=document.createElement('option');
        option.textContent=element;
        option.value=currencyChoices[element];
        select.appendChild(option);
    })
}

fillDropDown('currencyOne')
fillDropDown('currencyTwo')


async function getConvertRate(currencyOne,currencyTwo){
    const url=`https://v6.exchangerate-api.com/v6/${apiKey}/pair/${currencyOne}/${currencyTwo}`
    const response = await fetch(url);
    const data=await response.json()
    return data.conversion_rate
}

console.log(getConvertRate('EUR','GBP'))


async function convertCurrencies(){
    const currencyOne=document.getElementById('currencyOne').value;
    const currencyTwo=document.getElementById('currencyTwo').value;
    const convertAmount=document.getElementById('amount').value;

    const convertRate= await getConvertRate(currencyOne,currencyTwo);

    const convertResult=`${convertAmount*convertRate} ${currencyTwo}`;

    const result=document.createElement('p');
    result.textContent=convertResult;
    resultContainer.appendChild(result);
    console.log(currencyOne,currencyTwo,convertAmount,convertRate,convertResult)
}



const resultContainer=document.getElementById('result-container');
const convertBtn=document.getElementById('convert-btn');

convertBtn.addEventListener('click',convertCurrencies)