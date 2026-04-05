package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	encodedText string
	rows        int
}

func TestSurvivedRobotsHealths(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want string
	}{
		{
			name: "encodedText = 'ch   ie   pr', rows = 3",
			args: InputVal{
				encodedText: "ch   ie   pr",
				rows:        3,
			},
			want: "cipher",
		},
		{
			name: "encodedText = 'iveo    eed   l te   olc', rows = 4",
			args: InputVal{
				encodedText: "iveo    eed   l te   olc",
				rows:        4,
			},
			want: "i love leetcode",
		},
		{
			name: "encodedText = 'coding', rows = 1",
			args: InputVal{
				encodedText: "coding",
				rows:        1,
			},
			want: "coding",
		},
		{
			name: "encodedText = '     ie   pr', rows = 3",
			args: InputVal{
				encodedText: "     ie   pr",
				rows:        3,
			},
			want: " ip er",
		},
		{
			name: "wmihfwf bddhzaizuzhbuoovyyjstardqceaqzafdzihjbj ywly amkeemr jmvsfaavbpgiafgxzciwmrrtasthc hqfrtwoizoilw",
			args: InputVal{
				encodedText: "wmihfwf bddhzaizuzhbuoovyyjstardqceaqzafdzihjbj ywly amkeemr jmvsfaavbpgiafgxzciwmrrtasthc hqfrtwoizoilw",
				rows:        2,
			},
			want: "wammikhefewmfr  bjdmdvhszfaaiazvubzphgbiuaofogvxyzycjiswtmarrrdtqacsetahqcz ahfqdfzrithwjobijz oyiwllwy",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := decodeCiphertext(tt.args.encodedText, tt.args.rows); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("survivedRobotsHealths() = %v, want %v", got, tt.want)
			}
		})
	}
}
