package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	data []int
}

func TestValidUtf8(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want bool
	}{
		{
			name: "data = [197,130,1]",
			args: InputVal{
				data: []int{197, 130, 1},
			},
			want: true,
		},
		{
			name: "data = [235,140,4]",
			args: InputVal{
				data: []int{235, 140, 4},
			},
			want: false,
		},
		{
			name: "data = [237]",
			args: InputVal{
				data: []int{237},
			},
			want: false,
		},
		{
			name: "data = [10]",
			args: InputVal{
				data: []int{10},
			},
			want: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := validUtf8(tt.args.data); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("validUtf8() = %v, want %v", got, tt.want)
			}
		})
	}
}
