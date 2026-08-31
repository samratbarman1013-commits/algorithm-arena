#!/usr/bin/env node
/**
 * Algorithm Arena - Benchmark CLI
 * ================================
 * A Node.js CLI tool that benchmarks sorting algorithm performance
 * with randomly generated datasets of varying sizes.
 *
 * Usage:
 *   node benchmark/cli.js                  # Run all benchmarks
 *   node benchmark/cli.js --size 5000      # Custom dataset size
 *   node benchmark/cli.js --algo quick     # Run specific algorithm
 *   node benchmark/cli.js --json           # Output as JSON
 */

const { generateRandomArray, benchmark, ALGORITHMS } = require("./runner");

function parseArgs() {
  const args = process.argv.slice(2);
  const opts = { size: 1000, algo: null, json: false };
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--size" && args[i + 1]) {
      opts.size = parseInt(args[i + 1], 10);
      i++;
    } else if (args[i] === "--algo" && args[i + 1]) {
      opts.algo = args[i + 1];
      i++;
    } else if (args[i] === "--json") {
      opts.json = true;
    } else if (args[i] === "--help" || args[i] === "-h") {
      console.log(`Algorithm Arena Benchmark CLI

Usage:
  node benchmark/cli.js [options]

Options:
  --size <n>     Dataset size (default: 1000)
  --algo <name>  Run specific algorithm (${Object.keys(ALGORITHMS).join(", ")})
  --json         Output results as JSON
  --help, -h     Show this help message
`);
      process.exit(0);
    }
  }
  return opts;
}

function formatTable(results) {
  const nameWidth = Math.max(...results.map(r => r.name.length), 4) + 2;
  const timeWidth = 12;
  const sortedWidth = 8;

  const header =
    "Algorithm".padEnd(nameWidth) +
    "Time (ms)".padStart(timeWidth) +
    "Sorted?".padStart(sortedWidth);
  const separator = "-".repeat(header.length);

  let output = `${header}\n${separator}\n`;
  for (const r of results) {
    output +=
      r.name.padEnd(nameWidth) +
      r.timeMs.toFixed(3).padStart(timeWidth) +
      (r.correct ? "✓".padStart(sortedWidth) : "✗".padStart(sortedWidth)) +
      "\n";
  }
  return output;
}

function main() {
  const opts = parseArgs();
  const sizes = opts.size ? [opts.size] : [100, 1000, 5000];

  const allResults = [];

  for (const size of sizes) {
    const data = generateRandomArray(size);
    const algos = opts.algo ? { [opts.algo]: ALGORITHMS[opts.algo] } : ALGORITHMS;

    if (!opts.json) {
      console.log(`\n📊 Benchmarking with ${size.toLocaleString()} elements\n`);
    }

    const results = [];
    for (const [name, fn] of Object.entries(algos)) {
      if (!fn) {
        console.error(`Unknown algorithm: ${name}`);
        console.error(`Available: ${Object.keys(ALGORITHMS).join(", ")}`);
        process.exit(1);
      }
      const result = benchmark(fn, data);
      results.push({ name, ...result });
    }

    results.sort((a, b) => a.timeMs - b.timeMs);

    if (opts.json) {
      allResults.push({ size, results });
    } else {
      console.log(formatTable(results));
      const fastest = results[0];
      console.log(`🏆 Fastest: ${fastest.name} (${fastest.timeMs.toFixed(3)} ms)\n`);
    }
  }

  if (opts.json) {
    console.log(JSON.stringify(allResults, null, 2));
  }
}

main();
