import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

// let data;

// fetch('./processed_data.json')
// .then(response => response.json())
// .then(data => console.log(data))
// .catch(error => console.log(error));

const data = {
    "name": "AI/Machine Learning --- test",
    "children": [{
      "name": "Content Identification"
    }]
  };

const root = d3.hierarchy(data);

// You can create a hierarchy layout using d3.hierarchy and then use it for your visualization
// For example, to display the names of all nodes, you can do something like this:
root.descendants().forEach(node => {
  console.log(node.data.name);
});
const width = 928;
const height = width;

// Or if you want to create a basic tree diagram using D3, you can do:
const treeLayout = d3.tree().size([width, height]);
treeLayout(root);

// Now, you can access the data like this to draw your visualization
console.log(root.data.name); // This is the root node's name
console.log(root.children[0].data.name); // This is the name of the first child