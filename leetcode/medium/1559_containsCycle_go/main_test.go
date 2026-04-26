package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	grid [][]byte
}

func TestContainsCycle(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want bool
	}{
		{
			name: "1",
			args: InputVal{
				grid:  [][]byte{{'a', 'a', 'a', 'a'}, {'a', 'b', 'b', 'a'}, {'a', 'b', 'b', 'a'}, {'a', 'a', 'a', 'a'}},
			},
			want: true,
		},
		{
			name: "2",
			args: InputVal{
				grid: [][]byte{{'c', 'c', 'c', 'a'}, {'c', 'd', 'c', 'c'}, {'c', 'c', 'e', 'c'}, {'f', 'c', 'c', 'c'}},
			},
			want: true,
		},
		{
			name: "3",
			args: InputVal{
				grid: [][]byte{{'a', 'b', 'b'}, {'b', 'z', 'b'}, {'b', 'b', 'a'}},
			},
			want: false,
		},
		{
			name: "4",
			args: InputVal{
				grid: [][]byte{{'b','a','c'},{'c','a','c'},{'d','d','c'},{'b','c','c'}},
			},
			want: false,
		},
		{
			name: "5",
			args: InputVal{
				grid: [][]byte{{'c','a','d'},{'a','a','a'},{'a','a','d'},{'a','c','d'},{'a','b','c'}},
			},
			want: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := containsCycle(tt.args.grid); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("containsCycle() = %v, want %v", got, tt.want)
			}
		})
	}
}

/*


{
{'b','a','c'},
{'c','a','c'},
{'d','d','c'},
{'b','c','c'}



 */