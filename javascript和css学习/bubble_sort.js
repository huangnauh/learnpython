function bubbleSort(a){
    var n = a.length;
    var flag = n-1;
    while(flag){
        var i = flag;
        flag = 0;
        for(var j=0;j<i;j++){
            if(a[j] > a[j+1]){
                var temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
                flag = j;
            }
        }
    }
}