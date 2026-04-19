package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums1 []int
	nums2 []int
}

func TestMirrorDistance(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]",
			args: InputVal{
				nums1: []int{55, 30, 5, 4, 2},
				nums2: []int{100, 20, 10, 10, 5},
			},
			want: 2,
		},
		{
			name: "nums1 = [2,2,2], nums2 = [10,10,1]",
			args: InputVal{
				nums1: []int{2, 2, 2},
				nums2: []int{10, 10, 1},
			},
			want: 1,
		},
		{
			name: "nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]",
			args: InputVal{
				nums1: []int{30, 29, 19, 5},
				nums2: []int{25, 25, 25, 25, 25},
			},
			want: 2,
		},
		{
			name: "1",
			args: InputVal{
				nums1: []int{5, 4},
				nums2: []int{3, 2},
			},
			want: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxDistance(tt.args.nums1, tt.args.nums2); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("maxDistance() = %v, want %v", got, tt.want)
			}
		})
	}
}
