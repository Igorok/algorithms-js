package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	queries    []string
	dictionary []string
}

func TestTwoEditWords(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want []string
	}{
		{
			name: "1",
			args: InputVal{
				queries:    []string{"word", "note", "ants", "wood"},
				dictionary: []string{"wood", "joke", "moat"},
			},
			want: []string{"word", "note", "wood"},
		},
		{
			name: "2",
			args: InputVal{
				queries:    []string{"yes"},
				dictionary: []string{"not"},
			},
			want: []string{},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := twoEditWords(tt.args.queries, tt.args.dictionary); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("twoEditWords() = %v, want %v", got, tt.want)
			}
		})
	}
}
