package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	arr1 []int
	arr2 []int
}

func TestFindThePrefixCommonArray(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "arr1 = [1,10,100], arr2 = [1000]",
			args: InputVal{
				arr1: []int{1, 10, 100},
				arr2: []int{1000},
			},
			want: 3,
		},
		{
			name: "arr1 = [1,2,3], arr2 = [4,4,4]",
			args: InputVal{
				arr1: []int{1, 2, 3},
				arr2: []int{4, 4, 4},
			},
			want: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestCommonPrefix(tt.args.arr1, tt.args.arr2); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("longestCommonPrefix() = %v, want %v", got, tt.want)
			}
		})
	}
}
