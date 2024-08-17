const size = 5;
for (let i = 0; i <= size; i++) {
  for (let j = 0; j <= size; j++) {
    process.stdout.write(i * j + "");
  }
  console.log();
}
