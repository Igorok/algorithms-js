package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	words      []string
	target     string
	startIndex int
}

func TestClosestTarget(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "hello",
			args: InputVal{
				words:      []string{"hello", "i", "am", "leetcode", "hello"},
				target:     "hello",
				startIndex: 1,
			},
			want: 1,
		},
		{
			name: "leetcode",
			args: InputVal{
				words:      []string{"a", "b", "leetcode"},
				target:     "leetcode",
				startIndex: 0,
			},
			want: 1,
		},
		{
			name: "ate",
			args: InputVal{
				words:      []string{"i", "eat", "leetcode"},
				target:     "ate",
				startIndex: 0,
			},
			want: -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := closestTarget(tt.args.words, tt.args.target, tt.args.startIndex); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("closestTarget() = %v, want %v", got, tt.want)
			}
		})
	}
}
