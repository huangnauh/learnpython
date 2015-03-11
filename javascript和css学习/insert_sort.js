function insertSort(a){
    var n = a.length;
    for(var i=1;i<n;i++){
        var temp = a[i];
        var j = i;
        while(j>0 && temp<a[j-1]){
            a[j] = a[j-1];
            j--;
        }
        a[j] = temp;
    }
}