//javascriptµÝ¹é°æ±¾
Array.prototype.mergeSort = function(){
    var merge = function(left,right){
        var merged = [];
        while(left.length && right.length){
            merged.push(left[0] <= right[0] ? left.shift():right.shift());
        }
        return merged.concat(left.concat(right));
    }
    if (this.length < 2) return this;
    var mid = Math.floor(this.length/2);
    return merge(this.slice(0,mid).mergeSort(),this.slice(mid).mergeSort())
}