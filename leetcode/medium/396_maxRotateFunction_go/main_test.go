package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums []int
}

func TestMaxRotateFunction(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "1",
			args: InputVal{
				nums: []int{4, 3, 2, 6},
			},
			want: 26,
		},
		{
			name: "2",
			args: InputVal{
				nums: []int{100},
			},
			want: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxRotateFunction(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("maxRotateFunction() = %v, want %v", got, tt.want)
			}
		})
	}
}

/*


{
{'b','a','c'},
{'c','a','c'},
{'d','d','c'},
{'b','c','c'}



*/
