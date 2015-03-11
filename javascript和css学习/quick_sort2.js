//因为Javascript语言允许省略参数
//quickSortHelp和quickSort可以合并为一个函数，以上面的函数为例
function quickSort(a,first,last){
    if (a.length < 2) return a;
    first = (typeof first === "number" ? first : 0);
    last = (typeof last === "number" ? last : a.length-1);
    var p = partition(a,first,last);
    if (first < p-1){
        quickSort(a,first,p-1);
    }
    if(p+1 < last){
        quickSort(a,p+1,last);
    }
}