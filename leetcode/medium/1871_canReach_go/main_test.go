package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	s       string
	minJump int
	maxJump int
}

func TestFirstStableIndex(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want bool
	}{
		{
			name: "011010",
			args: InputVal{
				s:       "011010",
				minJump: 2,
				maxJump: 3,
			},
			want: true,
		},
		{
			name: "01101110",
			args: InputVal{
				s:       "01101110",
				minJump: 2,
				maxJump: 3,
			},
			want: false,
		},
		{
			name: "00111010",
			args: InputVal{
				s:       "00111010",
				minJump: 3,
				maxJump: 5,
			},
			want: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := canReach(tt.args.s, tt.args.minJump, tt.args.maxJump); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("canReach() = %v, want %v", got, tt.want)
			}
		})
	}
}
