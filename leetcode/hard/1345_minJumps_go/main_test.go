package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	arr []int
}

func TestMinJumps(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "arr = [100,-23,-23,404,100,23,23,23,3,404]",
			args: InputVal{
				arr: []int{100, -23, -23, 404, 100, 23, 23, 23, 3, 404},
			},
			want: 3,
		},
		{
			name: "arr = [7]",
			args: InputVal{
				arr: []int{7},
			},
			want: 0,
		},
		{
			name: "arr = [7,6,9,6,9,6,9,7]",
			args: InputVal{
				arr: []int{7, 6, 9, 6, 9, 6, 9, 7},
			},
			want: 1,
		},
		{
			name: "arr = [-76,3,66,-32,64,2,-19,-8,-5,-93,80,-5,-76,-78,64,2,16]",
			args: InputVal{
				arr: []int{-76, 3, 66, -32, 64, 2, -19, -8, -5, -93, 80, -5, -76, -78, 64, 2, 16},
			},
			want: 5,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minJumps(tt.args.arr); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("minJumps() = %v, want %v", got, tt.want)
			}
		})
	}
}
