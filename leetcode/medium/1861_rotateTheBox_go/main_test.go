package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	boxGrid [][]byte
}

func TestRotateTheBox(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want [][]byte
	}{
		{
			name: "1",
			args: InputVal{
				boxGrid: [][]byte{{'#', '.', '#'}},
			},
			want: [][]byte{{'.'},
				{'#'},
				{'#'}},
		},
		{
			name: "2",
			args: InputVal{
				boxGrid: [][]byte{{'#', '.', '*', '.'},
					{'#', '#', '*', '.'}},
			},
			want: [][]byte{{'#', '.'},
				{'#', '#'},
				{'*', '*'},
				{'.', '.'}},
		},
		{
			name: "3",
			args: InputVal{
				boxGrid: [][]byte{{'#', '#', '*', '.', '*', '.'},
					{'#', '#', '#', '*', '.', '.'},
					{'#', '#', '#', '.', '#', '.'}},
			},
			want: [][]byte{{'.', '#', '#'},
				{'.', '#', '#'},
				{'#', '#', '*'},
				{'#', '*', '.'},
				{'#', '.', '*'},
				{'#', '.', '.'}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := rotateTheBox(tt.args.boxGrid); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("rotateTheBox() = %v, want %v", got, tt.want)
			}
		})
	}
}
