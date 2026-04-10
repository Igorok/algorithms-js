package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	s         string
	knowledge [][]string
}

func TestSurvivedRobotsHealths(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want string
	}{
		{
			name: "1 (name)is(age)yearsold",
			args: InputVal{
				s:         "(name)is(age)yearsold",
				knowledge: [][]string{{"name", "bob"}, {"age", "two"}},
			},
			want: "bobistwoyearsold",
		},
		{
			name: "2 hi(name)",
			args: InputVal{
				s:         "hi(name)",
				knowledge: [][]string{{"a", "b"}},
			},
			want: "hi?",
		},
		{
			name: "3 (a)(a)(a)aaa",
			args: InputVal{
				s:         "(a)(a)(a)aaa",
				knowledge: [][]string{{"a", "yes"}},
			},
			want: "yesyesyesaaa",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := evaluate(tt.args.s, tt.args.knowledge); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("evaluate() = %v, want %v", got, tt.want)
			}
		})
	}
}
