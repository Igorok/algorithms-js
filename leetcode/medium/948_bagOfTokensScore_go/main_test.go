package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	tokens []int
	power  int
}

func TestMinIncrementForUnique(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "tokens = [100], power = 50",
			args: InputVal{
				tokens: []int{100},
				power:  50,
			},
			want: 0,
		},
		{
			name: "tokens = [200,100], power = 150",
			args: InputVal{
				tokens: []int{200, 100},
				power:  150,
			},
			want: 1,
		},
		{
			name: "tokens = [100,200,300,400], power = 200",
			args: InputVal{
				tokens: []int{100, 200, 300, 400},
				power:  200,
			},
			want: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := bagOfTokensScore(tt.args.tokens, tt.args.power); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("bagOfTokensScore() = %v, want %v", got, tt.want)
			}
		})
	}
}
