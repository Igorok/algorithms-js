package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	wordsContainer []string
	wordsQuery     []string
}

func TestStringIndices(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want []int
	}{
		{
			name: "1",
			args: InputVal{
				wordsContainer: []string{"abcd", "bcd", "xbcd"},
				wordsQuery:     []string{"cd", "bcd", "xyz"},
			},
			want: []int{1, 1, 1},
		},
		{
			name: "2",
			args: InputVal{
				wordsContainer: []string{"abcdefgh", "poiuygh", "ghghgh"},
				wordsQuery:     []string{"gh", "acbfgh", "acbfegh"},
			},
			want: []int{2, 0, 2},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := stringIndices(tt.args.wordsContainer, tt.args.wordsQuery); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("stringIndices() = %v, want %v", got, tt.want)
			}
		})
	}
}
