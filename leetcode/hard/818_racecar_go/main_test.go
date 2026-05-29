package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	target int
}

func TestRacecar(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "target = 3",
			args: InputVal{
				target: 3,
			},
			want: 2,
		},
		{
			name: "target = 6",
			args: InputVal{
				target: 6,
			},
			want: 5,
		},
		{
			name: "target = 6102",
			args: InputVal{
				target: 6102,
			},
			want: 39,
		},
		{
			name: "target = 5478",
			args: InputVal{
				target: 5478,
			},
			want: 50,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := racecar(tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("racecar() = %v, want %v", got, tt.want)
			}
		})
	}
}
