//选择数组开始的值作为基准
function partition(a,first,last){
    var p = first;
    left = first+1;
    right = last;
    var temp;
    while(left <= right){
        while(left <= right && a[left] <= a[p]){
            left++;
        }
        while(left <= right && a[right] > a[p]){
            right--;
        }
        if(left > right){
            break;
        }
        temp = a[left];
        a[left] = a[right];
        a[right] = temp;
        left++;
        right--;
   }
   temp = a[right];
   a[right] = a[first];
   a[first] = temp;
   return right;
}

function quickSortHelp(a,first,last){
    if(first >= last){
        return;
    }
    var p = partition(a,first,last);
    quickSortHelp(a,first,p-1);
    quickSortHelp(a,p+1,last);
}

function quickSort(a){
    quickSortHelp(a,0,a.length-1);    
}