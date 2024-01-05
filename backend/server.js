import fs from 'fs';
import csvParser from 'csv-parser';
import dotenv from 'dotenv';

dotenv.config();

const source = process.env.SOURCE
const sourceLocation = process.env.SOURCELOCATION

async function downloadCSV() {
  try {
    const response = await fetch(source);
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const csvData = await response.text();

    fs.writeFileSync(sourceLocation, csvData);
    
    console.log('CSV file downloaded successfully!');
  } catch (error) {
    console.error('Error downloading CSV:', error);
  }
}

async function loadCSV(){
  if (fs.existsSync(sourceLocation)) {
    fs.createReadStream(sourceLocation)
    .pipe(csvParser())
    .on('data', (row) => {
      console.log(row);
    })
    .on('end', () => {
      console.log('CSV file parsed successfully.');
    });
  } else {
    console.error('Source does not exists')
  }
}

downloadCSV()
  .then(() => loadCSV())