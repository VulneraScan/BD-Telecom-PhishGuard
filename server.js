const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;

const phishingKeywords = ["বিকাশ", "OTP", "লটারি", "জিতেছেন", "PIN", "সিম বন্ধ", "টাকা পাঠান", "কল করুন"];

app.use(cors());
app.use(express.json());

app.post('/analyze', (req, res) => {
  const { sms } = req.body;
  let suspicious = false;
  let foundKeywords = [];

  phishingKeywords.forEach(keyword => {
    if (sms.includes(keyword)) {
      suspicious = true;
      foundKeywords.push(keyword);
    }
  });

  res.json({
    suspicious,
    keywords: foundKeywords
  });
});

app.listen(port, () => {
  console.log(`PhishGuard API is running on http://localhost:${port}`);
});
