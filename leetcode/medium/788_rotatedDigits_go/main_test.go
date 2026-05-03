package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	n int
}

func TestRotatedDigits(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "n = 10",
			args: InputVal{
				n: 10,
			},
			want: 4,
		},
		{
			name: "n = 1",
			args: InputVal{
				n: 1,
			},
			want: 0,
		},
		{
			name: "n = 2",
			args: InputVal{
				n: 2,
			},
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := rotatedDigits(tt.args.n); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("rotatedDigits() = %v, want %v", got, tt.want)
			}
		})
	}
}
