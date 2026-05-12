package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums []int
}

func TestSeparateDigits(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want []int
	}{
		{
			name: "nums = [13,25,83,77]",
			args: InputVal{
				nums: []int{13, 25, 83, 77},
			},
			want: []int{1, 3, 2, 5, 8, 3, 7, 7},
		},
		{
			name: "nums = [7,1,3,9]",
			args: InputVal{
				nums: []int{7, 1, 3, 9},
			},
			want: []int{7, 1, 3, 9},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := separateDigits(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("separateDigits() = %v, want %v", got, tt.want)
			}
		})
	}
}
