//迭代版本
Array.prototype.mergeSort = function(){
    var merge = function(left,right){
        var merged = [];
        while(left.length && right.length){
            merged.push(left[0] <= right[0] ? left.shift():right.shift());
        }
        return merged.concat(left.concat(right));
    }
    var myarray = [];
    this.forEach(function(item){
        myarray.push([item]);
    });
    while(myarray.length > 1){
       myarray.push(merge(myarray.shift(),myarray.shift()))
    }
    return myarray[0];
}