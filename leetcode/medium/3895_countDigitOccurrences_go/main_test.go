package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums  []int
	digit int
}

func TestCountDigitOccurrences(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "1",
			args: InputVal{
				nums:  []int{12, 54, 32, 22},
				digit: 2,
			},
			want: 4,
		},
		{
			name: "2",
			args: InputVal{
				nums:  []int{1, 34, 7},
				digit: 9,
			},
			want: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := countDigitOccurrences(tt.args.nums, tt.args.digit); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("countDigitOccurrences() = %v, want %v", got, tt.want)
			}
		})
	}
}
