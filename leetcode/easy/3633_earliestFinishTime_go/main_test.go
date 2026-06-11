package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	landStartTime  []int
	landDuration   []int
	waterStartTime []int
	waterDuration  []int
}

func TestNumSubarraysWithSum(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]",
			args: InputVal{
				landStartTime:  []int{2, 8},
				landDuration:   []int{4, 1},
				waterStartTime: []int{6},
				waterDuration:  []int{3},
			},
			want: 9,
		},
		{
			name: "landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]",
			args: InputVal{
				landStartTime:  []int{5},
				landDuration:   []int{3},
				waterStartTime: []int{1},
				waterDuration:  []int{10},
			},
			want: 14,
		},
		{
			name: "3",
			args: InputVal{
				landStartTime:  []int{99},
				landDuration:   []int{59},
				waterStartTime: []int{99, 54},
				waterDuration:  []int{85, 20},
			},
			want: 158,
		},
		{
			name: "4",
			args: InputVal{
				landStartTime:  []int{90, 12},
				landDuration:   []int{39, 86},
				waterStartTime: []int{11, 86},
				waterDuration:  []int{44, 62},
			},
			want: 129,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := earliestFinishTime(tt.args.landStartTime, tt.args.landDuration, tt.args.waterStartTime, tt.args.waterDuration); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("earliestFinishTime() = %v, want %v", got, tt.want)
			}
		})
	}
}
