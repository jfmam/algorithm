const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', line => {
  input.push(line);
}).on('close', () => {
  const N = +input.shift();
  const arr = input.map(e => Array.from(e, x => +x));
  const visit = Array.from(Array(N), _ => Array(N).fill(false));

  const xPos = [-1, 1, 0, 0];
  const yPos = [0, 0, -1, 1];
  const dngs = [];
  let dng = 0;
  let cnt = 0;

  const dfs = (x, y) => {
    visit[x][y] = true;
    dng++;
    for (let i = 0; i < 4; i++) {
      let newX = x + xPos[i];
      let newY = y + yPos[i];
      if (newX < 0 || newX >= N || newY < 0 || newY >= N) continue;
      else if (!arr[newX][newY] || visit[newX][newY]) continue;
      else {
        dfs(newX, newY);
      }
    }
  };

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (arr[i][j] && !visit[i][j]) {
        cnt++;
        dfs(i, j);
        dngs.push(dng);
        dng = 0;
      }
    }
  }
  console.log(cnt);
  dngs.sort((a, b) => a - b).forEach(e => console.log(e));
});
