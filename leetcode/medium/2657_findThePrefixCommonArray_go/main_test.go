package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	A []int
	B []int
}

func TestFindThePrefixCommonArray(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want []int
	}{
		{
			name: "A = [1,3,2,4], B = [3,1,2,4]]",
			args: InputVal{
				A: []int{1, 3, 2, 4},
				B: []int{3, 1, 2, 4},
			},
			want: []int{0, 2, 3, 4},
		},
		{
			name: "A = [2,3,1], B = [3,1,2]",
			args: InputVal{
				A: []int{2, 3, 1},
				B: []int{3, 1, 2},
			},
			want: []int{0, 1, 3},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findThePrefixCommonArray(tt.args.A, tt.args.B); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("findThePrefixCommonArray() = %v, want %v", got, tt.want)
			}
		})
	}
}
