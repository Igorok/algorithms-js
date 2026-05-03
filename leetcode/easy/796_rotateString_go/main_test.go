package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	s    string
	goal string
}

func TestRotateString(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want bool
	}{
		{
			name: "1",
			args: InputVal{
				s:    "abcde",
				goal: "cdeab",
			},
			want: true,
		},
		{
			name: "2",
			args: InputVal{
				s:    "abcde",
				goal: "abced",
			},
			want: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := rotateString(tt.args.s, tt.args.goal); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("rotateString() = %v, want %v", got, tt.want)
			}
		})
	}
}
