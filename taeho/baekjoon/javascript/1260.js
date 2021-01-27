var rl = require("readline").createInterface({ input: process.stdin, output: process.stdout });
var input = [];
rl.on("line", line => {
  input.push(line);
}).on("close", () => {
  const [n, m, v] = input.shift().split(" ");
  const adj = Array.from(Array(+n + 1), () => new Array());
  for (let item of input) {
    const [x, y] = item.split(" ");
    adj[x].push(y);
    adj[y].push(x);
  }
  for (let item of adj) item.sort((a, b) => a - b);
  let result = dfs(
    +v,
    adj,
    Array.from(Array(+n + 1), () => false),
  );
  console.log(result);
});

function dfs(v, adj, visited) {
  visited[v] = true;
  for (let item of adj[v]) if (!visited[item]) return v + dfs(item, visited);
  return "";
}
