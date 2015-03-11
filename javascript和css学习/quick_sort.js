//选择数组中间的值作为基准
function partition(a,first,last){
    var p = Math.floor((first+last)/2),
        left = first,
        right = last,
        temp;
    while(left <= right){
        while(left <= right && a[left] < a[p]){
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
    return left;
}

function quickSortHelp(a,first,last){
    if(first >= last){
        return;
    }
    var p = partition(a,first,last);
    quickSortHelp(a,first,p-1);
    quickSortHelp(a,p,last);
}

function quickSort(a){
    quickSortHelp(a,0,a.length-1);    
}