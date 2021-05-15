
const pinataApiKey = "225995418f79d3537d7";
const pinataSecretApiKey = "Y250be06c3ea322ab67ec16d08e3c98e702064d4574a6783ab22bb2f9010a29ab";
const axios = require("axios");
const fs = require("fs");
const FormData = require("form-data");

const pinFileToIPFS = async () => {
  const url = `https://api.pinata.cloud/pinning/pinFileToIPFS`;
  let data = new FormData();
  data.append("file", fs.createReadStream("./STONE_TEMPLATE.jpeg"));
  const res = await axios.post(url, data, {
    maxContentLength: "Infinity", 
    headers: {
      "Content-Type": `multipart/form-data; boundary=${data._boundary}`,
      pinata_api_key: pinataApiKey, 
      pinata_secret_api_key: pinataSecretApiKey,
    },
  });
  console.log(res.data);
};

pinFileToIPFS();