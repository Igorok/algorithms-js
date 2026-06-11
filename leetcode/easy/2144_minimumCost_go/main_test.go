package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	cost []int
}

func TestMinimumCost(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "cost = [1,2,3]",
			args: InputVal{
				cost: []int{1, 2, 3},
			},
			want: 5,
		},
		{
			name: "cost = [6,5,7,9,2,2]",
			args: InputVal{
				cost: []int{6, 5, 7, 9, 2, 2},
			},
			want: 23,
		},
		{
			name: "cost = [5,5]",
			args: InputVal{
				cost: []int{5, 5},
			},
			want: 10,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minimumCost(tt.args.cost); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("minimumCost() = %v, want %v", got, tt.want)
			}
		})
	}
}
