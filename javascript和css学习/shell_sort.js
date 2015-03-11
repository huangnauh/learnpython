function shellSort(a){
    var n = a.length;
    var gap = Math.floor(n/2);
    while(gap){
        for(var i=gap;i<n;i+=gap){
            var j=i;
            var temp = a[i];
            while(j>0 && temp<a[j-gap]){
                a[j] = a[j-gap];
                j -= gap;
            }
            a[j]=temp;
        }
        gap = Math.floor(gap/2);
    }
}