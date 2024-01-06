<script setup>
    import csv from '../public/data.csv'
    console.log(csv)
</script>

<template>
    <div>
      <table v-if="csv.length > 0">
        <tbody>
          <tr v-for="(row, rowIndex) in csv" :key="rowIndex">
            <td v-for="(value, colIndex) in Object.values(row)" :key="colIndex">{{ value }}</td>
          </tr>
        </tbody>
      </table>
      <div v-else>
        <p>No data available</p>
      </div>
    </div>
</template>

<style>
</style>