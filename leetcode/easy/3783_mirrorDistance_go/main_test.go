package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	n int
}

func TestMirrorDistance(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "25",
			args: InputVal{
				n: 25,
			},
			want: 27,
		},
		{
			name: "10",
			args: InputVal{
				n: 10,
			},
			want: 9,
		},
		{
			name: "7",
			args: InputVal{
				n: 7,
			},
			want: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := mirrorDistance(tt.args.n); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("mirrorDistance() = %v, want %v", got, tt.want)
			}
		})
	}
}
