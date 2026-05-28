package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	word string
}

func TestFirstStableIndex(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "aaAbcBC",
			args: InputVal{
				word: "aaAbcBC",
			},
			want: 3,
		},
		{
			name: "abc",
			args: InputVal{
				word: "abc",
			},
			want: 0,
		},
		{
			name: "abBCab",
			args: InputVal{
				word: "abBCab",
			},
			want: 1,
		},
		{
			name: "zZ",
			args: InputVal{
				word: "zZ",
			},
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numberOfSpecialChars(tt.args.word); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("numberOfSpecialChars() = %v, want %v", got, tt.want)
			}
		})
	}
}
